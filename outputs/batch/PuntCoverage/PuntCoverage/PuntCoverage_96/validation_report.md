# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_96`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_96/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 194: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 194: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-135] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-152] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-172] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-236] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-232] for track '8' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-115] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-124] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-220] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-61] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-224] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-132] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-89] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-111] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-12] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-154] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '17' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-100] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-99] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [208-215] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-94] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-239] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-156] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-237] for track '33' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.