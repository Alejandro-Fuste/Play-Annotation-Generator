# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_58`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 118: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=146, end=142. Clamping end to start.
> - Action 'Action_None' range [129-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-166] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 205, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [205-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-265] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-202] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [138-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [189-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-329] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [155-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-30] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [151-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-160] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-252] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-300] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-245] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-254] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-287] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-251] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [183-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-320] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-243] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-273] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-243] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-273] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-324] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-281] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-274] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-324] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '39' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.