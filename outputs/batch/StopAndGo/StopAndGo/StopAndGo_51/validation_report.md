# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_51`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [5–21], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=22.
> - Segment 'Action_ThrowPass' for track '17' has invalid range: start=84, end=76. Clamping end to start.
> - Action 'Action_None' range [5-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-197] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-55] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [5-203] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [31-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [59-60] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SellStop' range [63-68] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [73-141] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [143-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [172-174] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-83] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-168] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-33] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-202] for track '13' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-74] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-51] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-57] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-34] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-70] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [84-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-176] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-196] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-111] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-128] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [109-129] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-139] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-140] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-197] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '39' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.