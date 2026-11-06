# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_109`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 220: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_CatchPunt' for track '25' has invalid range: start=171, end=169. Clamping end to start.
> - Action 'Action_None' range [228-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-99] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-288] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-298] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-144] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-194] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-242] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-194] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-217] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-130] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-173] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-294] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '25' starts at frame 172, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [172-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-299] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-292] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-251] for track '32' has 1 frames without a visible bounding box.
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