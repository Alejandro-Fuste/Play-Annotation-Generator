# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_128`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_128/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 258: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_None' range [109-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-264] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-282] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [285-290] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [294-295] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [297-300] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [309-335] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-257] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-292] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-301] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-335] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [338-348] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-146] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-218] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-41] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-108] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-38] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-260] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-306] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-316] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-298] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-337] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-358] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-229] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-262] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-298] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [307-325] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-250] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-271] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-290] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-294] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [300-322] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-346] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-344] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-357] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-273] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-358] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-296] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-321] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-322] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-326] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.