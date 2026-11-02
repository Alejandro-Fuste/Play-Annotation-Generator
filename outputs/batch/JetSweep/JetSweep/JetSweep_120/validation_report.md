# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_120`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 242: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [78-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-184] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [205-252] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-269] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-113] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-83] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-92] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.