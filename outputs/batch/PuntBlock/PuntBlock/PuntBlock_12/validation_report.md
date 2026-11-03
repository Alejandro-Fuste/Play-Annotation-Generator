# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_12`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 167 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '17' has invalid range: start=202, end=192. Clamping end to start.
> - Action 'Action_None' range [21-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [82-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-255] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-257] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-249] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [91-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-144] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-194] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-260] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-143] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-188] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-253] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [255-263] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-269] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-153] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-212] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-263] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-204] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [209-223] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-154] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-219] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-206] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-225] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-263] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-185] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-250] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-183] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-229] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-244] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-206] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-228] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-252] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-167] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-218] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-263] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-183] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-225] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-186] for track '44' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-205] for track '44' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [207-228] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [234-250] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-185] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-240] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-217] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-269] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-224] for track '48' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-230] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-245] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-262] for track '51' has 2 frames without a visible bounding box.
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
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.