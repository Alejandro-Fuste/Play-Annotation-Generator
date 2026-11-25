# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_161`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_161/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 322: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=178, end=37. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '18' has invalid range: start=185, end=37. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '18' has invalid range: start=185, end=56. Clamping end to start.
> - Segment 'Action_Handoff' for track '18' has invalid range: start=185, end=66. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '20' has invalid range: start=198, end=103. Clamping end to start.
> - Action 'Action_None' range [26-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-293] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-234] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-251] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-286] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-230] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-251] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [200-293] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-253] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-256] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-279] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-289] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-281] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '27' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_161'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.