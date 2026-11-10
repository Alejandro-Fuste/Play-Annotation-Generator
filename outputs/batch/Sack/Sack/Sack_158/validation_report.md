# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_158`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_158/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 50 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-120] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [108-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-76] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [68-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-103] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-116] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-115] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '29' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.