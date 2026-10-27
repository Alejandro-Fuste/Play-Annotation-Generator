# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_8`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '0' (LT) duration 106 frames exceeds threshold 90 frames [start=114, end=219].
> - Action 'Action_PreSnap' range [0-9] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-296] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-313] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-321] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [148-235] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-224] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-283] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-161] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-43] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-180] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-229] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-139] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-27] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-158] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [126-151] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [172-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-243] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-146] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-257] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [132-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-195] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-161] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-296] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-214] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-168] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-184] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-242] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [171-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-221] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-208] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-302] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-328] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-256] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-260] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-275] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-273] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-327] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.