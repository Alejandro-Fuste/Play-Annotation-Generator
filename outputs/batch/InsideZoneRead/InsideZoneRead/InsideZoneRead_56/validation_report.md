# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_56`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 99 frames exceeds threshold 90 frames [start=133, end=231].
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 99 frames exceeds threshold 90 frames [start=133, end=231].
> - Segment 'Action_BallSnap' for track '10' has invalid range: start=131, end=60. Clamping end to start.
> - Action 'Action_PreSnap' range [0-39] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-171] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-201] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-290] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-259] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-294] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [213-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-267] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [270-283] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-204] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-199] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-19] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-60] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-170] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-257] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-277] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-295] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-206] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-176] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-243] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-270] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-211] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-258] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-291] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-265] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-277] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-283] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-296] for track '22' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.