# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_80`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 162: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [2-40] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-47] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [57-82] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [92-103] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [119-160] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [164-169] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [177-263] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [282-327] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-52] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-298] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [2-23] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-55] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-3] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-153] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-162] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-231] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-11] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-238] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-12] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-10] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-18] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-126] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-143] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [228-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-253] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-262] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-42] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-34] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-125] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-215] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [220-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-77] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-87] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-154] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-165] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-119] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-130] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-137] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-142] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-175] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-216] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-223] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-231] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-300] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-241] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-324] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-308] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-309] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-322] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.