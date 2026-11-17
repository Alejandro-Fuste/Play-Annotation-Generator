# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_111`
- **Input XML**: `outputs/batch/Power/Power/Power_111/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 223: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 224: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-360] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-337] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-346] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-351] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-365] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-343] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-308] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-225] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-334] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-243] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-340] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-352] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-353] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-263] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-389] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-258] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-355] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-217] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-246] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-342] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-319] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-345] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [211-226] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [211-240] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [243-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-131] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-352] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-344] for track '25' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.