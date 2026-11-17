# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_232`
- **Input XML**: `outputs/batch/Power/Power/Power_232/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 30 |
| Ball Tracks | 2 |
| CSV events parsed | 7 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 466: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 466: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 466: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_DownBlock' for track '22' has invalid range: start=227, end=200. Clamping end to start.
> - Action 'Action_PreSnap' range [12-254] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-281] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [143-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [172-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [143-172] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-230] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-204] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-197] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-212] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-226] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-298] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '29' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.