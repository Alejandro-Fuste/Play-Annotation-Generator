# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_57`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_57/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [150-162] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [137-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-180] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [117-157] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [160-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [163-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-180] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-64] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '28' has 1 frames without a visible bounding box.
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