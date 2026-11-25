# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_213`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_213/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 426: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=125, end=121. Clamping end to start.
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=198, end=137. Clamping end to start.
> - Action 'Action_None' range [122-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-189] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-258] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-232] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [161-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [174-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-41] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-200] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 199, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [199-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-219] for track '16' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_213'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.