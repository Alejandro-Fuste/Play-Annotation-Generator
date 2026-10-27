# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_48`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_48/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 30 |
| Ball Tracks | 1 |
| CSV events parsed | 19 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Segment 'Action_BallCarry' for track '1' has invalid range: start=231, end=227. Clamping end to start.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [194–207], lower_priority='Action_PullBlock' annotated_start=200, effective_Action_PullBlock_start=208.
> - Action 'Action_DownBlock' range [200-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [229-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-285] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [200-215] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [217-233] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [240-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [245-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-260] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-342] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-288] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-315] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-272] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-325] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-201] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-274] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-302] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [306-328] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [208-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [216-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [236-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [239-248] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [252-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-337] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-465] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [467-468] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [471-472] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-112] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [200-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-307] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-240] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-264] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-304] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-254] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-301] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-273] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-321] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-272] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [277-304] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-274] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-349] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-473] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [475-479] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-373] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-479] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-479] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-316] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-406] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-479] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-369] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [379-471] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [475-479] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-437] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [439-440] for track '28' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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