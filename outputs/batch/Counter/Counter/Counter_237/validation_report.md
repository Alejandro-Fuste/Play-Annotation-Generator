# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_237`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_237/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [87–106], lower_priority='Action_DownBlock' annotated_start=89, effective_Action_DownBlock_start=107.
> - Segment 'Action_BallCarry' for track '21' has invalid range: start=129, end=117. Clamping end to start.
> - Action 'Action_None' range [87-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-179] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-155] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-266] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-247] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-159] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [89-169] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-238] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-185] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '29' has 1 frames without a visible bounding box.
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