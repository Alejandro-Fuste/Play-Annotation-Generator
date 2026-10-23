# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_1`
- **Input XML**: `output_showcase_final/PuntCoverage/PuntCoverage_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '25' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [2-204] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-226] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-46] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-285] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-28] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-45] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-52] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-157] for track '7' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [160-202] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-285] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-110] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-144] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-197] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-114] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-142] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-22] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-166] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [168-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-137] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-168] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-70] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [72-81] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-139] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-139] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-153] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-230] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [2-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [24-25] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [34-49] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-120] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-254] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-177] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-262] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [194-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-245] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-211] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [209-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-285] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-267] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-281] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-299] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-285] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-299] for track '36' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.