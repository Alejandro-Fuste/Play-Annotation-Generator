# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_248`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_248/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [23–39], lower_priority='Action_ZoneBlock' annotated_start=26, effective_Action_ZoneBlock_start=40.
> - Action 'Action_None' range [23-96] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-88] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-195] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-152] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-217] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-177] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-234] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-181] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-34] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-231] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-192] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-212] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-219] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-202] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-237] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '28' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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