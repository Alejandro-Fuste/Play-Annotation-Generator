# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_37`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 126 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [26–40], lower_priority='Action_RunBlock' annotated_start=34, effective_Action_RunBlock_start=41.
> - Action 'Action_None' range [26-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-236] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-63] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-91] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-258] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-298] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-260] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-265] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-281] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-244] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-212] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-186] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-257] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-260] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-163] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-54] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [34-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [43-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [53-113] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [34-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [90-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-294] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [34-48] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [53-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [158-247] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [255-258] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [260-278] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [280-287] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [290-291] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [293-297] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-287] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-211] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-211] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-222] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-254] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-221] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-288] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-293] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-286] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-296] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '38' has 2 frames without a visible bounding box.
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