# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_32`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 34: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [180–184], lower_priority='Action_PassBlock' annotated_start=183, effective_Action_PassBlock_start=185.
> - Action 'Action_None' range [180-217] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-245] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-262] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-321] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BreakInside' range [201-226] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BreakInside' range [228-324] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-348] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-368] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-419] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-336] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ClearToEdge' range [201-277] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-232] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-368] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-382] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-411] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-419] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-209] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-273] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 180, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [180-184] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-225] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [191-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [200-201] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-367] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-249] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-274] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-249] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-398] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [403-408] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-412] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-307] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-345] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-419] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-341] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-344] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-368] for track '24' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.