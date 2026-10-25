# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_113`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [42–43], lower_priority='Action_RunBlock' annotated_start=43, effective_Action_RunBlock_start=44.
> - Overlapping action conflict at frame 43 for track '21': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
> - Segment 'Action_BootAway' for track '21' has invalid range: start=69, end=62. Clamping end to start.
> - Segment 'Action_ThrowPass' for track '21' has invalid range: start=89, end=62. Clamping end to start.
> - Action 'Action_None' range [42-260] for track '0' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [42-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-259] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-257] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-219] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-258] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-221] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-202] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [204-269] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-298] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [44-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-67] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-257] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-108] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-299] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [43-75] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-80] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [87-276] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [43-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [77-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-41] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [43-54] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [56-62] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [72-76] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [82-85] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-142] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-296] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.