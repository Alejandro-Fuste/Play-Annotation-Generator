# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_121`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_121/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-120] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [91-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [110-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-103] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.