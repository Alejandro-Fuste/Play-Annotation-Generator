# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_233`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_233/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 466: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '9' has invalid range: start=125, end=121. Clamping end to start.
> - Action 'Action_ZoneBlock' range [125-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-252] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [161-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-251] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-256] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_Handoff' for track '9' starts at frame 151, but the player has no visible bounding box on this frame.
> - Action 'Action_Handoff' range [151-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-287] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-299] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-204] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-222] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-272] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 204, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [204-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-121] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-19] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-33] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-62] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-270] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-273] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-271] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-262] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [271-284] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-294] for track '28' has 2 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_233'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.