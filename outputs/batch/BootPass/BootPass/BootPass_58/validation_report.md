# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_58`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 44 |
| Ball Tracks | 2 |
| CSV events parsed | 21 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 96: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [137–153], lower_priority='Action_RunBlock' annotated_start=146, effective_Action_RunBlock_start=154.
> - Action 'Action_None' range [162-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-192] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-277] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [146-207] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [214-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-260] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-223] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-219] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-271] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [146-152] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [146-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [180-268] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [270-280] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [154-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [187-246] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [251-278] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-16] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-38] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-274] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-166] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-272] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-154] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-221] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-262] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-277] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [164-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-274] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-253] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-298] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-271] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-219] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-258] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-274] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-324] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-307] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-300] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-275] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-329] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-282] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-321] for track '43' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [314-320] for track '45' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.