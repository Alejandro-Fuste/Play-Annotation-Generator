# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_111`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_111/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 224: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 224: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-287] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-295] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-250] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-287] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-254] for track '6' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CatchPunt' range [177-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [201-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [260-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-265] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-35] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-81] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-299] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-203] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-216] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-163] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-167] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-180] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-201] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-282] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-294] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-38] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-182] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-278] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-294] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-258] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-281] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-154] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-294] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-201] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [227-241] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [243-244] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [247-249] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-290] for track '30' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.