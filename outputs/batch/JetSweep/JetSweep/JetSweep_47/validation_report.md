# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_47`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [120–132], lower_priority='Action_ZoneBlock' annotated_start=121, effective_Action_ZoneBlock_start=133.
> - Action 'Action_None' range [120-167] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-299] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-257] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-273] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-218] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-147] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [152-156] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-177] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-195] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-219] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-153] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-155] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [123-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-278] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-287] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-227] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-280] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-280] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.