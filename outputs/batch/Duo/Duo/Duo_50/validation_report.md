# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_50`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 102: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_BlockSecondLevel' range [141-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [163-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-268] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-268] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-172] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-213] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [157-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-268] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-123] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [157-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [164-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [182-188] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-268] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-172] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-192] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-245] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-182] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-200] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-219] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-268] for track '30' has 2 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.