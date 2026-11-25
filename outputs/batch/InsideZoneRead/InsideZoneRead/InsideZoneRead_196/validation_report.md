# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_196`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_196/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallSnap' for track '12' has invalid range: start=171, end=88. Clamping end to start.
> - Action 'Action_None' range [171-340] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-354] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 171, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [171-198] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-359] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-312] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-350] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-201] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [210-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-328] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-295] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-332] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-235] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-351] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-240] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-323] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-348] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [174-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [201-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-316] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-359] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-181] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-340] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-272] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_196'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.