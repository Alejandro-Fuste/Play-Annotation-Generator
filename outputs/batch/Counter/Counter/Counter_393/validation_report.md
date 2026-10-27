# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_393`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_393/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 788: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - Row 788: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [69–85], lower_priority='Action_DownBlock' annotated_start=72, effective_Action_DownBlock_start=86.
> - Validation warning: Action 'Action_DownBlock' for track '18' (DT2) duration 92 frames exceeds threshold 90 frames [start=72, end=163].
> - Action 'Action_None' range [69-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-169] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [194-220] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-243] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-259] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-30] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-68] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-102] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [69-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-138] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [135-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-103] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-71] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [72-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-148] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [72-94] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-71] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [72-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [134-153] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-232] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [72-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-94] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-148] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-199] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-228] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-244] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-132] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-174] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-243] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-261] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-161] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-191] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-228] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-243] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-267] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '41' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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