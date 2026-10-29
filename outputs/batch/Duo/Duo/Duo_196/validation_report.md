# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_196`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_196/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 274 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 274 as fallback play end.
> - Action 'Action_PreSnap' range [0-151] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-237] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-260] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-274] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-207] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [164-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [170-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-136] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-232] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-189] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-69] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-131] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-172] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-274] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-254] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-127] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-147] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-236] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-274] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-135] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-164] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-151] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-232] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-207] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-229] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-246] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-251] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-257] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-240] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-253] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-274] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-227] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-254] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-249] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-274] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.