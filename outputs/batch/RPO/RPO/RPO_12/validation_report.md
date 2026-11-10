# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_12`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [40-132] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-111] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-136] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-179] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-156] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-95] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-182] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-134] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-111] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-68] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-134] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-194] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '24' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.