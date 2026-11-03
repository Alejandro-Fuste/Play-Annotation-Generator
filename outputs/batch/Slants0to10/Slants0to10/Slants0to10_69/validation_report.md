# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_69`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [1–17], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=18.
> - Action 'Action_None' range [1-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-192] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-237] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-94] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-111] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-143] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-172] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [1-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-39] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-128] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-95] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-70] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-94] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-59] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [18-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [79-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-120] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-178] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-115] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-151] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-140] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-125] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-237] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-225] for track '34' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.