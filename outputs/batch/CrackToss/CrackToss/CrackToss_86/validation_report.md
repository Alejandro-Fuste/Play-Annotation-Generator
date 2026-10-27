# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_86`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_86/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 141 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 399 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 174: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 174: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
> - Action 'Action_None' range [143-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-291] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-399] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-163] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-263] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-279] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-372] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [147-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '4' starts at frame 237, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [237-354] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [143-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [147-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [204-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [218-236] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-294] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-259] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-233] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-354] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [143-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-366] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [143-201] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-209] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-265] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-289] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-300] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-399] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [174-235] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-245] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [247-253] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [265-266] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [268-270] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-384] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [386-388] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [391-399] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-399] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-362] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-300] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-313] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-399] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-297] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-207] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [210-220] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-256] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-399] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-297] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-313] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-399] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-268] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-284] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [287-317] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-391] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-202] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-261] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-302] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-305] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-315] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-202] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-261] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-364] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-368] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-291] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-316] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [319-399] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-313] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [320-327] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-351] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [282-286] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-306] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-311] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-386] for track '32' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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