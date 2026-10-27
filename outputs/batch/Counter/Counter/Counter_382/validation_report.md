# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_382`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_382/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 766: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [170–182], lower_priority='Action_DownBlock' annotated_start=173, effective_Action_DownBlock_start=183.
> - Action 'Action_None' range [170-243] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-366] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [173-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-228] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [222-320] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-325] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-215] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-326] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-294] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-360] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [173-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [186-241] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [252-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-230] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-366] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [183-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [191-216] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [222-254] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-270] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-288] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-363] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-330] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-347] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-287] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-298] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [300-306] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-328] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-375] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-361] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-389] for track '23' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.