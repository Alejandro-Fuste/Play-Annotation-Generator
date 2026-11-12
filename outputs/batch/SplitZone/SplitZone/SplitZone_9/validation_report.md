# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_9`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [76–86], lower_priority='Action_ZoneBlock' annotated_start=79, effective_Action_ZoneBlock_start=87.
> - Action 'Action_None' range [76-146] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-133] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-275] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-256] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [124-295] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-151] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [154-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-108] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-156] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-250] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-285] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-299] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-178] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-140] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-224] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [79-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-196] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [114-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-206] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-299] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-243] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.