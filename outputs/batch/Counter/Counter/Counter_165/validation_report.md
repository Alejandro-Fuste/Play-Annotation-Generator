# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_165`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_165/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 332: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [73-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-269] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-136] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-126] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-214] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-266] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-269] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [73-248] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-134] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [235-236] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [244-252] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [75-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [75-88] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-116] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [120-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-161] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [75-96] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-173] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-262] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [75-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-109] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [111-201] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-65] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-70] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-202] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-220] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-246] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-234] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-198] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-262] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-196] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.