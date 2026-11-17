# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_144`
- **Input XML**: `outputs/batch/Power/Power/Power_144/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 290: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_DownBlock' range [59-101] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-123] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [59-113] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [114-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-149] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-84] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-155] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-210] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-84] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [59-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-104] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-139] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-160] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-178] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-202] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-140] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-210] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-26] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-63] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-156] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-121] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-182] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-155] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-201] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-210] for track '22' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.