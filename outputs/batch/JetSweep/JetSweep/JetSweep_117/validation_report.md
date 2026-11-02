# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_117`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 235: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '10' has invalid range: start=128, end=125. Clamping end to start.
> - Segment 'Action_BallSnap' for track '16' has invalid range: start=126, end=34. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '16' has invalid range: start=128, end=34. Clamping end to start.
> - Segment 'Action_BallCarry' for track '19' has invalid range: start=152, end=149. Clamping end to start.
> - Action 'Action_None' range [126-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-213] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-161] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-188] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-190] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-298] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-249] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-188] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-185] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-215] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-221] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-125] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-189] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [123-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [144-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-251] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-255] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-297] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '33' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.