# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_130`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_130/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
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
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [112-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [128-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-116] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-150] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-63] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-140] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [141-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '28' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.