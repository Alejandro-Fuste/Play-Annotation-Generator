# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_163`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_163/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [21-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-49] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-171] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-177] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-168] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-28] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-102] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-170] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '28' has 1 frames without a visible bounding box.
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