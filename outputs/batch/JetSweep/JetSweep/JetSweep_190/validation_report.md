# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_190`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_190/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 49 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [10–23], lower_priority='Action_ZoneBlock' annotated_start=11, effective_Action_ZoneBlock_start=24.
> - Action 'Action_None' range [10-216] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-236] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-58] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-50] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-51] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-53] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-50] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-71] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [11-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-61] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-45] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [37-244] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [10-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-207] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-268] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-224] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [192-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-183] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-269] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-218] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [230-269] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-205] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-198] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-227] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-230] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-224] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-258] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-222] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-246] for track '42' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-240] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-265] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-252] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '47' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.