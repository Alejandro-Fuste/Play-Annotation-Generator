# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_88`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_88/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=74, end=73. Clamping end to start.
> - Action 'Action_PreSnap' range [0-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [83-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-276] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-128] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-153] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-229] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-219] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-259] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-215] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-199] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-207] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-146] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-112] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-198] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [97-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '20' starts at frame 122, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [122-149] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [158-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-84] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-103] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-147] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-169] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-203] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-284] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-205] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-215] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-201] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-338] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-342] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-223] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-359] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-359] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.