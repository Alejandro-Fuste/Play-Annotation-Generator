# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_121`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_121/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 244: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Segment 'Action_BallCarry' for track '17' has invalid range: start=219, end=206. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [173–188], lower_priority='Action_DownBlock' annotated_start=177, effective_Action_DownBlock_start=189.
> - Action 'Action_None' range [173-255] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-358] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-238] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [177-261] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [177-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [210-261] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-307] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-295] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-355] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [177-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-220] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-259] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-381] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [384-385] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-238] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-346] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-376] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [189-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-261] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [177-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-297] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-234] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-265] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-242] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-284] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-292] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-308] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-315] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-213] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-381] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-218] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-246] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-273] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-365] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-301] for track '30' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.