# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_234`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_234/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=238, end=105. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '19' has invalid range: start=250, end=105. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '19' has invalid range: start=250, end=118. Clamping end to start.
> - Segment 'Action_Handoff' for track '19' has invalid range: start=250, end=133. Clamping end to start.
> - Action 'Action_ZoneBlock' range [94-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-30] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-269] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-218] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 239, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [239-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-258] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 251, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [251-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '19' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_234'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.