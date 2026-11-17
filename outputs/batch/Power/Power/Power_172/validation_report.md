# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_172`
- **Input XML**: `outputs/batch/Power/Power/Power_172/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 346: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [29-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-175] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-179] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 149, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [149-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-122] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-151] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-141] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-256] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-242] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-259] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '30' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.