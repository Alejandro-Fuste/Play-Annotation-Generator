# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_15`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 34 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 32: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-190] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-138] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-186] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-102] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-199] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-153] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-113] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-129] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-174] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-197] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-231] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-263] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-209] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-224] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-257] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '34' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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