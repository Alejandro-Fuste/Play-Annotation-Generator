# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_32`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 41 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [102-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-103] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-120] for track '25' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.