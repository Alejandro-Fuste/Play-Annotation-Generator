# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_13`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [179–194], lower_priority='Action_ZoneBlock' annotated_start=181, effective_Action_ZoneBlock_start=195.
> - Action 'Action_None' range [179-315] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-338] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-355] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-247] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-271] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-345] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-287] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-293] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-275] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-302] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-338] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-350] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-274] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-359] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [217-218] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '11' starts at frame 195, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [195-197] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [230-232] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-280] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-310] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-292] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-321] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-333] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-356] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-293] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-336] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-346] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-357] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-38] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-223] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [229-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [233-246] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-256] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-273] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-338] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-296] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-316] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [319-320] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-327] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-348] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-333] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-340] for track '31' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.