# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_56`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 274 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 114: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 274 as fallback play end.
> - Action 'Action_None' range [123-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-232] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-217] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [153-238] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-263] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-257] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-216] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-274] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-231] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-274] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-263] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [269-274] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-22] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-69] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-89] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-95] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [126-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [138-158] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-220] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-244] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-186] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-212] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [123-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-216] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-274] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-216] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-149] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-253] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-236] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-216] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-231] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-260] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-232] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-255] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [262-268] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-263] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-274] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-274] for track '30' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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