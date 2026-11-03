# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_15`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_SecureRecovery' for track '33' has invalid range: start=164, end=101. Clamping end to start.
> - Action 'Action_None' range [0-122] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-30] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-41] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-257] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [259-267] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [59-63] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-70] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-80] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-109] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-14] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-53] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-55] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-20] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-27] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-80] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-99] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [48-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [76-128] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [133-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [141-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [150-252] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-66] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [0-243] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [245-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-73] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [0-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [0-14] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [21-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-218] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [0-6] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-7] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-62] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-82] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-37] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-33] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-41] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-67] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-60] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-74] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-265] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-235] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [79-269] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-200] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-101] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-143] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-166] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-146] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-246] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '43' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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