# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_107`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 215: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
> - Row 216: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 216: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 216: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - Row 216: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_None' range [158-184] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-389] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-270] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-369] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-372] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-389] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-168] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-389] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-200] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-388] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-246] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-389] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-375] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-388] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-374] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-293] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [298-387] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-343] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-347] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-373] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.