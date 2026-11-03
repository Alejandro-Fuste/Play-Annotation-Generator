# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_49`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_SellStop' range [73-77] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [96-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [214-216] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [221-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-111] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-58] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-136] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [151-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [176-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [180-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-176] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-162] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-222] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-86] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-182] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-223] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-51] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [57-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [178-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-171] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-167] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-37] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '28' has 2 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.