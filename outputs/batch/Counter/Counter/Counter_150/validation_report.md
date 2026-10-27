# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_150`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_150/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [136-236] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-168] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-216] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [137-176] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-254] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [137-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-192] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-202] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-218] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-53] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-135] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 136, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [136-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-162] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [137-162] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-244] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-273] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-211] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-35] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-43] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-85] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 136, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [136-140] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-115] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [159-206] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-218] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-184] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-189] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-200] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-238] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-285] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-291] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '36' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.